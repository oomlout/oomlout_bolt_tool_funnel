rem if overwrite doesn't exist make it 0
if not defined overwrite set overwrite=0

if %overwrite%==0 (
    echo oolc_process no overwrite
    oolc_process.py 
)
if %overwrite%==1 (
    echo oolc_process overwrite
    oolc_process.py -overwrite
)

