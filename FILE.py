import platform,os,time
bit = platform.architecture()[0]
if bit == '64bit':
    import file
elif bit == '32bit':
    import file32
