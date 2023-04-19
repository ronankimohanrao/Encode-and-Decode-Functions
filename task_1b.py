def decoding_function(input_string):
    value_variable = ''
    output_variable = ''
    for i in range(len(input_string)):
        if (value_variable == ''):
             value_variable = input_string[i]
        else:
            for j in range(0,int(value_variable)):
                output_variable = output_variable+input_string[i]
                value_variable = ''   
    return(output_variable)                
         
print(decoding_function())

def encoding_function(input_string):
  value_variable = ''
  output_variable = ''
  count_variable = 0
  for i in range(len(input_string)):
    if (value_variable==''):
      count_variable = 1
      value_variable = input_string[i]
    elif (input_string[i]==value_variable):
      count_variable +=1
    else:
      output_variable = output_variable+str(count_variable)+value_variable
      count_variable = 1
      value_variable = input_string[i]
  output_variable = output_variable+str(count_variable)+value_variable
  return(output_variable)

print(encoding_function(""))

