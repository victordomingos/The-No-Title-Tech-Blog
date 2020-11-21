brew install libjpeg-turbo
brew install zlib
export LDFLAGS="-L/usr/local/opt/jpeg-turbo/lib"
export CPPFLAGS="-I/usr/local/opt/jpeg-turbo/include"
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"
export CPATH=`xcrun --show-sdk-path`/usr/include
pip3.8 uninstall pillow; 
CFLAGS="${CFLAGS} -mavx2" pip3.8 install --upgrade --no-cache-dir --force-reinstall --no-binary :all: --compile pillow-simd
echo "Let's check if Pillow is using libjpeg_turbo now?"
python3.8 -c "from PIL import features; print(features.check_feature('libjpeg_turbo'))"

