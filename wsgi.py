#!/usr/bin/python3
"""module for wsgi"""


from app import main

if __name__ == "__main__":
    app = main()
    app.run()
