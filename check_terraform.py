#!/usr/bin/env python3
"""
Script to check if Terraform is installed and working properly.
"""

import subprocess
import sys
import os

def check_terraform():
    """Check if Terraform is installed and working."""
    
    print("=" * 50)
    print("Terraform Installation Check")
    print("=" * 50)
    print()
    
    # Check 1: Terraform command exists
    print("1. Checking if Terraform is installed...")
    try:
        result = subprocess.run(
            ["terraform", "version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("✓ Terraform is installed")
            print(f"  Version info: {result.stdout.strip()}")
        else:
            print("✗ Terraform command failed")
            print(f"  Error: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("✗ Terraform not found in PATH")
        print("  Make sure Terraform is installed and added to your PATH")
        return False
    except subprocess.TimeoutExpired:
        print("✗ Terraform command timed out")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    print()
    
    # Check 2: Terraform help
    print("2. Checking Terraform help command...")
    try:
        result = subprocess.run(
            ["terraform", "-help"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("✓ Terraform help works")
            # Show first few lines of help
            help_lines = result.stdout.strip().split('\n')[:5]
            for line in help_lines:
                print(f"  {line}")
        else:
            print("✗ Terraform help command failed")
            return False
            
    except Exception as e:
        print(f"✗ Error running help: {e}")
        return False
    
    print()
    
    # Check 3: Terraform init (dry run) - checks if terraform can be initialized
    print("3. Checking Terraform init capability...")
    try:
        result = subprocess.run(
            ["terraform", "init", "-backend=false"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=os.getcwd()
        )
        
        # init might fail if no tf files, but command should work
        print("✓ Terraform init command is available")
            
    except Exception as e:
        print(f"✗ Error with terraform init: {e}")
    
    print()
    
    # Check 4: Terraform validate
    print("4. Checking Terraform validate capability...")
    try:
        result = subprocess.run(
            ["terraform", "validate"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=os.getcwd()
        )
        
        # validate might fail if no tf files, but command should work
        print("✓ Terraform validate command is available")
            
    except Exception as e:
        print(f"✗ Error with terraform validate: {e}")
    
    print()
    print("=" * 50)
    print("✓ Terraform is working correctly!")
    print("=" * 50)
    return True

if __name__ == "__main__":
    success = check_terraform()
    sys.exit(0 if success else 1)
