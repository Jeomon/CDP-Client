from generator import CDPGenerator
import asyncio

def main():
    cdp_generator = CDPGenerator()
    cdp_generator.generate()
    print("Generation complete.")

if __name__ == "__main__":
    main()
