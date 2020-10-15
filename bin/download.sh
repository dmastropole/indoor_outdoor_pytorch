FILE=data/indoor_outdoor.zip
if test -f "$FILE"; then
	echo "$FILE already exists. Skipping download"
else
	wget https://dresearch.blob.core.windows.net/public-indoor-outdoor/indoor_outdoor.zip -P data
	unzip data/indoor_outdoor.zip -d data
fi
