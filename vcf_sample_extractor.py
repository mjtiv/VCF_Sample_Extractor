#!/usr/bin/env python3.6

"""
PROGRAM: VCF Sample Extractor
DESCRIPTION: Program parses apart a vcf extracting specific samples of interest (defined by user)
    and prints these samples to a new vcf file. 

AUTHOR: M. Joseph Tomlinson IV

DATE CREATED: 4-20-2018
"""


def parsing_input_parameter_file():
    """ 
    Parses through the paramter file to return a dictionary
    of the input parameters
    :param none: automatically opens file
    :return dictionary: dictionary of file names for analysis
    """

    input_file = open('VCF_Extractor_Parameter_File.txt', 'r')

    print ("Parsed Lines from User")
    
    for line in input_file:
        if line.startswith("--"):
            line=line.rstrip('\n')
            # just printing user inpt for validation
            print (line)
            parsed_parameters=line.split("--")

            for x in range(1, len(parsed_parameters)):
                inputs = parsed_parameters[x].split(" ")
                
                if inputs[0] == "VCF_Input_File":
                    vcf_input_file = inputs[1] 

                elif inputs[0] == "Samples_to_Extract_File":
                    samples_to_extract_file = inputs[1]

                elif inputs[0] == "VCF_Output_File":
                    vcf_output_file = inputs[1]
                

    # Skip anything else
    else:
        pass

    input_file.close()

    #Printing 
    print ("Name of VCF input File is: ", vcf_input_file)
    print ("Name of Samples to Extract File: ", samples_to_extract_file)
    print ("Name of VCF Output File is: ", vcf_output_file)
    
    return{'vcf_input_file':vcf_input_file, 'samples_to_extract_file':samples_to_extract_file,
           'vcf_output_file':vcf_output_file}



def extract_sample_names(parameter_stuff):
    """
    Opens up the samples to extract to file and gets the
    list of samples
    :param parameter_stuff: program parameter dictionary (get sample list file)
    :return samples_to_extract_list: list of samples to extract from vcf file
    """

    samples_list_file = parameter_stuff['samples_to_extract_file']

    input_file = open(samples_list_file, 'r')

    samples_to_extract_list = []

    # Read through the list of samples
    for line in input_file:

        # Removing newline from data
            sample = line.rstrip('\n')

            samples_to_extract_list.append(sample)

    print ("The list of samples to extract are: ")
    print (samples_to_extract_list)

    input_file.close()

    return (samples_to_extract_list)


def extract_print_new_vcf_file(parameter_stuff, samples_to_extract_list):
    """
    Function opens up the original vcf file and parses through the data
    extracting the specific samples of interst from the file and outputs
    the data to a new vcf file
    :param parameter_stuff: parameter information for analysis (file names)
    :param samples_to_extract_list: list of samples to extract from file
    :return NONE
    """

    input_vcf_file = parameter_stuff['vcf_input_file']

    output_vcf_file = parameter_stuff['vcf_output_file']

    # VCF Input File
    vcf_input_file = open(input_vcf_file, 'r')
    # VCF Output File
    vcf_output_file = open(output_vcf_file, 'w')

    # Get indices of samples of interest
    samples_list_indices = []

    for line in vcf_input_file:
        
        #Get Header from file
        
        if line.startswith(("##", "#", " #", "'#")) and not line.startswith('#CHROM'):
            vcf_output_file.write(line)
        
        if line.startswith('#CHROM'):

            # Strip newline from line
            line = line.rstrip('\n')

            # Split data on the tab
            parsed_line = line.split('\t')

            # Get header for variant stuff
            header_variant_info = parsed_line[:9]

            # Convert header to a string for writing to file
            header_variant_info = ('\t'.join(map(str,header_variant_info)))

            # Write to new vcf file
            vcf_output_file.write(header_variant_info + '\t')

            # Getting the sample names from file
            header_sample_list = parsed_line[9:]
  
            #setting initial movement value
            x = 0
            for header_sample in header_sample_list:

                for sample in samples_to_extract_list:

                    # Finding matching samples and get the index location
                    if sample == header_sample:
                        
                        # Write sample name to header of new vcf file
                        vcf_output_file.write(str(header_sample) + "\t")

                        # Get the index of the sample
                        samples_list_indices.append(x)

                    # Just keep moving through lists
                    else:
                        pass

                #Move the counter for next iteration
                x += 1
                    
            print ("Printing the indices of samples")
            print (samples_list_indices)        
            # Move the output file to a new line
            vcf_output_file.write("\n")
    
        else:
            line = line.rstrip('\n')
            parsed_line = line.split('\t')

            # Get header for variant stuff
            variant_info = parsed_line[:9]

            # Get samples data
            samples_data = parsed_line[9:]

            # Convert header to a string for writing to file
            variant_info = ('\t'.join(map(str,variant_info)))

            # Write to new vcf file
            vcf_output_file.write(variant_info + '\t')
            
            for value in samples_list_indices:
                vcf_output_file.write(str(samples_data[value]) + '\t')

            vcf_output_file.write("\n")

    vcf_input_file.close()
    vcf_output_file.close()
    
    return()



def main():

    print ("Running VCF Sample Extractor!")

    #########################################################
    # Opens the parameter file to get file name
    print("Opening the parameter file")
    parameter_stuff = parsing_input_parameter_file()

    # Retrieving the parameters from the parameter file parsing output
    print ("Extract the list of samples to get")
    samples_to_extract_list = extract_sample_names(parameter_stuff)

    # Parsing VCF to get the information of interest
    print ("Filtering the original vcf for the samples of interest")
    extract_print_new_vcf_file(parameter_stuff, samples_to_extract_list)

    print ("Program Done Running")
    

main()
















