import traceback

from django.shortcuts import render

def print_exception(e):
    stack = traceback.extract_stack()
    print(f"Error in '{stack[-2][2]}'. {e}")

# Create your views here.
