#!/bin/bash

# Rails Upgrade Assistant - Build Archive Script
# Creates a zip file excluding git, build, and system files

set -e # Exit on error

echo "📦 Building Rails Upgrade Assistant archive..."

# Create build directory if it doesn't exist
mkdir -p build

# Create the zip archive
echo "🗜️  Compressing files..."
zip -r build/rails-upgrade-assistant.zip . \
  -x '*.git/*' \
  -x '.gitignore' \
  -x '*build/*' \
  -x '*bin/*' \
  -x '.DS_Store'

echo "✅ Archive created: build/rails-upgrade-assistant.zip"
echo ""

# Show file info
echo "📊 Archive information:"
ls -lh build/rails-upgrade-assistant.zip

echo ""
echo "📄 Contents preview (first 20 files):"
unzip -l build/rails-upgrade-assistant.zip | head -20

echo ""
echo "✨ Done!"
