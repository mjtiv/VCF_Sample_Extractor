PROGRAM: VCF Sample Extractor
DESCRIPTION: Program parses apart a vcf extracting specific samples of interest (defined by user)
    and prints these samples to a new vcf file. 

AUTHOR: M. Joseph Tomlinson IV

DATE CREATED: 4-20-2018

Required Files for Running

1. Original VCF file being parsed
2. TXT file of list of names of samples to extract
3. VCF_Extractor_Parameter_File.txt

Running Program 

First change the parameter files parameters. Very simple just update to your file names on the specific parameter line. 
All parameters are spaced seperated from the input parameter defined on that specific line.

-Running Locally
Open up the program and run in python, all files must be in the same directory as the program. Output will be placed where
you designate the output file (your/pathway/of/interest/new_vcf_file_name.txt).

-Running in HPC Environment
Update the parameter file (save) and then submit a sbatch/qsub file using the following command "python vcf_sample_extractor.py"
in the sbatch/qsub file.

#Output Files
New vcf file (technically txt file) with the ONLY the samples of interest will be outputted. 

