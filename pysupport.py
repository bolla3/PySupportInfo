#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # #
#    Created by bolla3 (bolla3.net)	  # 
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # 


#First declaring some variables to store text in

error_msg = raw_input("enter any error message you get here: ")
additional_info = raw_input("enter any additional information that you think can help troubleshooting here: ")
done = raw_input("Type 'exit' to close")
#Opening the text document for writing

f = open('supportinfo.txt', 'w')

#Writing the info stored in the variables

f.write(error_msg + "\n")
f.write(additional_info)


#And then closing the text document

f.close()
