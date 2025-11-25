"""Tests for CDP Generator"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from generator.service import CDPGenerator


@pytest.fixture
def mock_protocol_data():
    """Mock CDP protocol data"""
    return {
        "version": {"major": "1", "minor": "3"},
        "domains": [
            {
                "domain": "Page",
                "description": "Actions and events related to the inspected page",
                "types": [
                    {
                        "id": "FrameId",
                        "type": "string",
                        "description": "Unique frame identifier"
                    },
                    {
                        "id": "Frame",
                        "type": "object",
                        "properties": [
                            {"name": "id", "type": "string"},
                            {"name": "url", "type": "string"},
                            {"name": "name", "type": "string", "optional": True}
                        ]
                    }
                ],
                "commands": [
                    {
                        "name": "enable",
                        "description": "Enables page domain notifications"
                    },
                    {
                        "name": "navigate",
                        "description": "Navigates current page to the given URL",
                        "parameters": [
                            {"name": "url", "type": "string"}
                        ],
                        "returns": [
                            {"name": "frameId", "$ref": "FrameId"}
                        ]
                    }
                ],
                "events": [
                    {
                        "name": "loadEventFired",
                        "parameters": [
                            {"name": "timestamp", "type": "number"}
                        ]
                    },
                    {
                        "name": "frameNavigated",
                        "parameters": [
                            {"name": "frame", "$ref": "Frame"}
                        ]
                    }
                ]
            },
            {
                "domain": "Network",
                "deprecated": False,
                "types": [
                    {
                        "id": "RequestId",
                        "type": "string"
                    }
                ],
                "commands": [
                    {
                        "name": "enable",
                        "description": "Enables network tracking"
                    }
                ],
                "events": [
                    {
                        "name": "requestWillBeSent",
                        "parameters": [
                            {"name": "requestId", "$ref": "RequestId"}
                        ]
                    }
                ]
            },
            {
                "domain": "DeprecatedDomain",
                "deprecated": True,
                "commands": [],
                "events": []
            }
        ]
    }


@pytest.fixture
def generator(tmp_path):
    """Create a CDPGenerator instance with temporary paths"""
    gen = CDPGenerator()
    gen.protocol_path = tmp_path / "protocol"
    gen.client_path = tmp_path / "client"
    return gen


class TestCDPGeneratorInitialization:
    """Test CDP Generator initialization"""
    
    def test_generator_initializes_correctly(self):
        """Test that generator initializes with correct paths"""
        gen = CDPGenerator()
        assert gen.protocol_path == Path("./protocol")
        assert gen.client_path == Path("./client")
        assert gen.env is not None
        assert gen.type_generator is not None
        assert gen.event_generator is not None
        assert gen.method_generator is not None
        assert gen.client_generator is not None
    
    def test_generator_has_jinja_environment(self):
        """Test that generator has Jinja2 environment configured"""
        gen = CDPGenerator()
        assert gen.env.trim_blocks is True
        assert gen.env.lstrip_blocks is True


class TestCDPGeneratorDomains:
    """Test CDP Generator domain loading"""
    
    @patch('httpx.get')
    def test_domains_property_loads_protocols(self, mock_get, generator, mock_protocol_data):
        """Test that domains property loads protocol data"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        domains = generator.domains
        
        assert len(domains) > 0
        assert mock_get.call_count == 2  # browser_protocol and js_protocol
    
    @patch('httpx.get')
    def test_domains_property_filters_deprecated(self, mock_get, generator, mock_protocol_data):
        """Test that domains property includes deprecated domains (filtering happens later)"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        domains = generator.domains
        
        # Should include all domains initially
        domain_names = [d['domain'] for d in domains]
        assert 'Page' in domain_names
        assert 'Network' in domain_names
        assert 'DeprecatedDomain' in domain_names
    
    @patch('httpx.get')
    def test_domains_property_caches_result(self, mock_get, generator, mock_protocol_data):
        """Test that domains property caches the result"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        # Access domains multiple times
        domains1 = generator.domains
        domains2 = generator.domains
        
        # Should only call httpx.get once per URL (2 total)
        assert mock_get.call_count == 2
        assert domains1 is domains2  # Same object due to caching
    
    @patch('httpx.get')
    def test_domains_property_handles_network_error(self, mock_get, generator):
        """Test that domains property handles network errors gracefully"""
        mock_get.side_effect = Exception("Network error")
        
        domains = generator.domains
        
        # Should return empty list on error
        assert domains == []


class TestCDPGeneratorFileWriting:
    """Test CDP Generator file writing"""
    
    def test_write_file_creates_directory(self, generator):
        """Test that write_file creates parent directories"""
        test_path = generator.protocol_path / "test_domain" / "test.py"
        content = "# Test content"
        
        generator.write_file(test_path, content)
        
        assert test_path.exists()
        assert test_path.read_text() == content
    
    def test_write_file_overwrites_existing(self, generator):
        """Test that write_file overwrites existing files"""
        test_path = generator.protocol_path / "test.py"
        
        generator.write_file(test_path, "First content")
        generator.write_file(test_path, "Second content")
        
        assert test_path.read_text() == "Second content"
    
    def test_write_file_creates_nested_directories(self, generator):
        """Test that write_file creates nested directory structures"""
        test_path = generator.protocol_path / "a" / "b" / "c" / "test.py"
        
        generator.write_file(test_path, "Nested content")
        
        assert test_path.exists()
        assert test_path.parent.exists()


class TestCDPGeneratorDomainTypes:
    """Test CDP Generator domain type generation"""
    
    @patch('httpx.get')
    def test_generate_domain_types_creates_files(self, mock_get, generator, mock_protocol_data):
        """Test that generate_domain_types creates necessary files"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        domain = mock_protocol_data['domains'][0]  # Page domain
        
        with patch.object(generator.type_generator, 'generate_types', return_value="# Types"):
            with patch.object(generator.event_generator, 'generate_event_types', return_value="# Event Types"):
                with patch.object(generator.method_generator, 'generate_method_types', return_value="# Method Types"):
                    generator.generate_domain_types(domain)
        
        # Check that files were created
        domain_dir = generator.protocol_path / "page"
        assert (domain_dir / "__init__.py").exists()
        assert (domain_dir / "types.py").exists()
        assert (domain_dir / "events" / "__init__.py").exists()
        assert (domain_dir / "events" / "types.py").exists()
        assert (domain_dir / "methods" / "__init__.py").exists()
        assert (domain_dir / "methods" / "types.py").exists()
    
    @patch('httpx.get')
    def test_generate_domain_types_uses_snake_case(self, mock_get, generator, mock_protocol_data):
        """Test that domain names are converted to snake_case"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        # Create a domain with camelCase name
        domain = {
            "domain": "DOMStorage",
            "types": [],
            "commands": [],
            "events": []
        }
        
        with patch.object(generator.type_generator, 'generate_types', return_value=""):
            with patch.object(generator.event_generator, 'generate_event_types', return_value=""):
                with patch.object(generator.method_generator, 'generate_method_types', return_value=""):
                    generator.generate_domain_types(domain)
        
        # Directory should be in snake_case
        assert (generator.protocol_path / "dom_storage").exists()


class TestCDPGeneratorDomainServices:
    """Test CDP Generator domain service generation"""
    
    @patch('httpx.get')
    def test_generate_domain_services_creates_files(self, mock_get, generator, mock_protocol_data):
        """Test that generate_domain_services creates service files"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        domain = mock_protocol_data['domains'][0]  # Page domain
        
        with patch.object(generator.event_generator, 'generate_event_services', return_value="# Event Services"):
            with patch.object(generator.method_generator, 'generate_method_services', return_value="# Method Services"):
                generator.generate_domain_services(domain)
        
        domain_dir = generator.protocol_path / "page"
        assert (domain_dir / "events" / "service.py").exists()
        assert (domain_dir / "methods" / "service.py").exists()


class TestCDPGeneratorClient:
    """Test CDP Generator client generation"""
    
    @patch('httpx.get')
    def test_generate_client_creates_files(self, mock_get, generator, mock_protocol_data):
        """Test that generate_client creates client files"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        with patch.object(generator.client_generator, 'generate_methods', return_value="# Methods"):
            with patch.object(generator.client_generator, 'generate_events', return_value="# Events"):
                generator.generate_client()
        
        assert (generator.client_path / "__init__.py").exists()
        assert (generator.client_path / "methods.py").exists()
        assert (generator.client_path / "events.py").exists()
    
    @patch('httpx.get')
    def test_generate_client_filters_deprecated_domains(self, mock_get, generator, mock_protocol_data):
        """Test that generate_client filters out deprecated domains"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        with patch.object(generator.client_generator, 'generate_methods', return_value="") as mock_methods:
            with patch.object(generator.client_generator, 'generate_events', return_value=""):
                generator.generate_client()
        
        # Check that deprecated domains were filtered
        called_domains = mock_methods.call_args[0][0]
        domain_names = [d['domain'] for d in called_domains]
        assert 'DeprecatedDomain' not in domain_names
        assert 'Page' in domain_names
        assert 'Network' in domain_names


class TestCDPGeneratorProtocol:
    """Test CDP Generator protocol generation"""
    
    @patch('httpx.get')
    def test_generate_protocol_processes_all_domains(self, mock_get, generator, mock_protocol_data):
        """Test that generate_protocol processes all non-deprecated domains"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        with patch.object(generator, 'generate_domain_types') as mock_types:
            with patch.object(generator, 'generate_domain_services') as mock_services:
                generator.generate_protocol()
        
        # Should be called for each non-deprecated domain
        assert mock_types.call_count == 2  # Page and Network
        assert mock_services.call_count == 2
    
    @patch('httpx.get')
    def test_generate_protocol_skips_deprecated_domains(self, mock_get, generator, mock_protocol_data):
        """Test that generate_protocol skips deprecated domains"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        with patch.object(generator, 'generate_domain_types') as mock_types:
            with patch.object(generator, 'generate_domain_services'):
                generator.generate_protocol()
        
        # Check that deprecated domain was not processed
        processed_domains = [call[0][0]['domain'] for call in mock_types.call_args_list]
        assert 'DeprecatedDomain' not in processed_domains


class TestCDPGeneratorFullGeneration:
    """Test full CDP generation workflow"""
    
    @patch('httpx.get')
    def test_generate_creates_complete_structure(self, mock_get, generator, mock_protocol_data):
        """Test that generate() creates complete CDP client structure"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        with patch.object(generator, 'generate_protocol') as mock_protocol:
            with patch.object(generator, 'generate_client') as mock_client:
                generator.generate()
        
        # Both protocol and client should be generated
        mock_protocol.assert_called_once()
        mock_client.assert_called_once()
    
    @patch('httpx.get')
    def test_generate_order_is_correct(self, mock_get, generator, mock_protocol_data):
        """Test that generate() calls methods in correct order"""
        mock_response = Mock()
        mock_response.json.return_value = mock_protocol_data
        mock_get.return_value = mock_response
        
        call_order = []
        
        def track_protocol():
            call_order.append('protocol')
        
        def track_client():
            call_order.append('client')
        
        with patch.object(generator, 'generate_protocol', side_effect=track_protocol):
            with patch.object(generator, 'generate_client', side_effect=track_client):
                generator.generate()
        
        # Protocol should be generated before client
        assert call_order == ['protocol', 'client']
