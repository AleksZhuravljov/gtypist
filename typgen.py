import sys

def typgen(file_name, n_lines, comand):
    
    with open(file_name, 'r') as file_in:
        lines = [line for line in file_in]
        
    with open(file_name[0:-4] + '.typ', 'w') as file_out:
        
        file_out.write('G:Menu\n\n')
        
        parts = ['Part_0']       
        file_out.write('*:' + parts[-1] + '\n')
        file_out.write('B:' + parts[-1] + '\n' + comand + ':\n')       
        
        for i in range(len(lines)):
            
            if (i + 1) % n_lines == 0:
                file_out.write('G:Menu\n\n')
                parts.append('Part_' + str((i + 1) // n_lines))
                file_out.write('*:' + parts[-1] + '\n')
                file_out.write('B:' + parts[-1] + '\n' + comand + ':\n')
                
            file_out.write(' :'+ lines[i])
            
        file_out.write('G:Menu\n\n')
        
        file_out.write('*:Menu\n')
        file_out.write('M:\"' + file_name[0:-4] +' (' + comand + ')'+ '\"\n')
        for part in parts:
            file_out.write(' :' + part + ' \"' + part + '\"\n')
        file_out.write(' :Exit \"Exit\"\n\n')
        
        file_out.write('*:Exit\n')
        file_out.write('X:')       
    
    
typgen(file_name=sys.argv[1], n_lines=int(sys.argv[2]), comand=sys.argv[3])
