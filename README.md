# data_cleaning
> [!NOTE]
Purpose of this code is to clean BLS data. Important parameters are OCODE (Occupational Employment Codes) and FIPS (localities). <br />
Rather than inputting one file by one, or chucking multiple relative paths into a list, this program directly takes all .JSON files within a designated folder and clean.
Very efficient when you have multiple .JSON files to clean.

## REQUIRED LIBRARIES
!pip install json
!pip install pandas
!pip install re
!pip install glob
