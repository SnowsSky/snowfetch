#!/bin/bash

APP_NAME="snowfetch"
INSTALL_DIR="$HOME/.local/bin"
SCRIPT_PATH="$INSTALL_DIR/$APP_NAME"

echo "📂 Setting up '$APP_NAME'..."

mkdir -p "$INSTALL_DIR"

cp "$APP_NAME.py" "$SCRIPT_PATH"
chmod +x "$SCRIPT_PATH"

echo "✅ Script installed in $INSTALL_DIR"

if ! grep -q "$INSTALL_DIR" <<< "$PATH"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
    echo "🔧 Added '$INSTALL_DIR' to your PATH."
fi

if ! grep -q "alias $APP_NAME=" "$HOME/.bashrc"; then
    echo "alias $APP_NAME='python3 $SCRIPT_PATH'" >> "$HOME/.bashrc"
    echo "alias $APP_NAME='python3 $SCRIPT_PATH'" >> "$HOME/.zshrc"
    echo "🔗 Created an alias: You can now run '$APP_NAME' from anywhere!"
fi


export PATH="$INSTALL_DIR:$PATH"
source "$HOME/.bashrc" 2>/dev/null || source "$HOME/.zshrc" 2>/dev/null

echo "🎉 Installation complete! You can now use '$APP_NAME'"
echo ""


echo "🛑 To uninstall '$APP_NAME', run these commands:"
echo "rm -f $HOME/.local/bin/$APP_NAME"
echo "sed -i '/alias $APP_NAME=/d' ~/.bashrc ~/.zshrc"
echo "source ~/.bashrc 2>/dev/null || source ~/.zshrc 2>/dev/null"
echo ""

echo "🚀 Enjoy using '$APP_NAME'!"
