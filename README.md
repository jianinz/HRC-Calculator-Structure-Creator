# HRC-Calculator-Structure-Creator
A set of helpful scripts that automating prize structure for HRC calculator

# Packages Installation

## Windows
### Install Python on Windows
Make sure you have Python installed already on Windows. Go to Start and enter _cmd_ in the search bar. Click Command Prompt. Enter the following command in the command prompt:
```
python --version
```
An example of the output is:
```
Python 3.10.10
```

### Setup Windows Terminal (Optional)
If you used to use MS-DOS and Command Prompt, you could skip this part. If you are a Mac/Linux user, it's highly recommend to install PowerShell as it works similar as _fish_, _zsh_, _bash_

Windows Terminal will choose PowerShell as default. 
https://learn.microsoft.com/en-us/windows/terminal/install


## MacOS
### Install Python on Mac

1. Open Terminal.
2. Type the following command:
```
python --version
```
If Python is installed, the command outputs the version number.
```
Python 3.10.1
```
If Python is not installed, install it.
```
brew install python3
```

# Copy Prize Information

## GG Poker

![image](https://github.com/user-attachments/assets/7fbbb7d0-3508-46fd-8d22-3899083e960a)

1. Visit **PokerCraft**->**Completed Tournaments**, find out the one you want to review.
2. Click on **Players**, select the hightlighted text and copy it.
3. Replace hardcoded string _data_ variable with the copied one in __GG_Structure_Creator.py__ and save the modifed script.
4. Go to your terminal, run
```
python GG_Structure_Creator.py
```
An example of the output is:
```json
{
    "prizes": {
        "1": "418.77",
        "2": "332.26",
        "3": "263.65",
        "4": "209.21",
        "5": "166.02",
        "6": "131.74",
        "7": "104.53",
        "8": "82.95",
        "9": "65.82",
        "10": "52.23",
        "11": "49.62"
    }
}
```
5. Locate **custom.json** file in your HRC Calculator plugins folder
> On Windows ```C:\Users\XXX\HoldemResources\.metadata\.plugins\net.holdemresources.calculator\structuredata```
Not sure about Mac, please contribute. Thanks : )
6. Replace _prizes_ json blob with the generated one, please make sure _bountyType_ set correctly before loading it in the HRC Calculator!!
7. Load the **custom.json** in your HRC Calculator.
8. Voila, no more manual input for large field tournaments : )

![image](https://github.com/user-attachments/assets/78180153-e52b-4649-8649-dcb33cef8187)

