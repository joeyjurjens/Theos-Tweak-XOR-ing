
# Theos-Tweak-Offset-Encryptor

### Sample Output:
![EncryptScript](https://imgur.com/WVhEmmS.png)

This is a simple Python script that has been written for my Mod Menu Template: https://github.com/joeyjurjens/iOS-Mod-Menu-Template-for-Theos

The encryption method is XOR, so it's not the best & safest encryption. 
However, if you handle the decryption well, it'll be hard enough for most leechers to decrypt the offsets.

## Usage in theos:
In your makefile, add this:
```makefile
# Run python script to encrypt offsets
internal-package-check::
	@python3 encrypt.py
```
## What you have to do:
If you use it on my Mod Menu Template, you have to write the decryption in:

- Menu.mm
- Macros.h

If you use it in a own theos template, you might have to edit the script.
The pattern is explained in the script file.
You'd also need to write your own description

## Possibilities
The script has a pattern that find offsets, which means you could use another encryption method if you'd like. Note that if you do this, you have to keep in mind that you'll need to decrypt the offsets aswell, so make sure you can do that too in the languages theos supports.

## Testing this script
I included a Tweak.xm in the repo, so you can clone this repo and run the script:
```
python3 encrypt.py
```