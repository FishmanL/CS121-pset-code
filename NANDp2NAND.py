import sys
import os


"""
CS121 HW2 2017
THE TODO's are optional, since you can choose which helper functions you want.
However, you must still come up with a way to meet the specification.
The included code helps make properly formated strings, opens and closes files,
and writes to files.
"""

'''
These make properly formated strings given triples of variables.
'''
def make_AND_statement(output,input1,input2):
    return  "{} := {} AND {}".format(output, input1, input2)

def make_OR_statement(output,input1,input2):
    return  "{} := {} OR {}".format(output, input1, input2)

def make_XOR_statement(output,input1,input2):
    return  "{} := {} XOR {}".format(output, input1, input2)

def make_NAND_statement(output,input1,input2):
    return  "{} := {} NAND {}".format(output, input1, input2)


'''
Takes a file object f and a NAND line,
and writes a NAND line to the file with a newline character
'''
def write_NAND_line(f,line):
    f.write("%s\n" % line)

"""
Writes NAND triple (not line) to file
"""
def write_NAND_triple(f,output,x1,x2):
    line = make_NAND_statement(output,x1,x2)
    write_NAND_line(f,line)

'''
Writes any kind of line to file
'''
def write_DEBUG_line(f,line):
    f.write("%s\n" % line)


'''
Returns vars from OR line
'''
def parse_OR(line):
    # ASSUMES SPACING!
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2


"""
Returns vars from XOR line
"""
def parse_XOR(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2

"""
Returns vars from AND line
"""
def parse_AND(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2



"""
Returns vars from NAND line
"""
def parse_NAND(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR() and parse_XOR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2

"""
Returns vars from MAJ line
"""
def parse_MAJ(line):
    # ASSUMES SPACING!
    words = line.split()
    output = words[0]
    variables = words[2].split(',')
    index = variables[0].index('(')
    input1 = variables[0][index+1:]
    input2 = variables[1]
    input3 = variables[2][:len(variables[2]) - 1]
    return output, input1, input2, input3

"""
MOTIVATING QUESTION: WHY DO THE BELOW FUNCTIONS ALL TAKE A COUNTER ARGUMENT?
"""

'''
Implement a function that takes a number
and adds a special prefix to it
'''
def get_var_name(counter):
    return "var_{}".format(counter)

NANDline = "{} := {} NAND {}\n"

"""
Takes an AND line and writes a series of NAND lines to file
"""
def write_AND_as_NAND(f, line, counter):
    # TODO
    return counter

"""
Takes an AND triple and writes a series of NAND lines to file
"""
def write_AND_triple_as_NAND(f, output,input1,input2,counter):
    # TODO
    return counter

"""
Takes an XOR line and writes a series of NAND lines to file
"""
def write_XOR_as_NAND(f, line, counter):
    lvars = parse_XOR(line)
    u = get_var_name(counter)
    v = get_var_name(counter + 1)
    w = get_var_name(counter + 2)
    write_NAND_line(f, make_NAND_statement(u, lvars[1], lvars[2]))
    write_NAND_line(f, make_NAND_statement(v, lvars[1], u))
    write_NAND_line(f, make_NAND_statement(w, lvars[2], u))
    write_NAND_line(f, make_NAND_statement(lvars[0], v, w))
    return (counter + 2)

"""
Takes an OR line and writes a series of NAND lines to file
"""
def write_OR_as_NAND(f, line, counter):
    # TODO
    return counter

"""
Takes an OR triple and writes a series of NAND lines to file
"""
def write_OR_triple_as_NAND(f,output,input1,input2,counter):
    # TODO
    return counter

"""
Takes a MAJ line and writes a series of NAND lines to file
"""
def write_MAJ_as_NAND(f, line,counter):
    lvars = parse_MAJ(line)
    d = get_var_name(counter)
    e = get_var_name(counter + 1)
    t = get_var_name(counter + 2)
    g = get_var_name(counter + 3)
    h = get_var_name(counter + 4)
    write_NAND_line(f, make_NAND_statement(d, lvars[1], lvars[2]))
    write_NAND_line(f, make_NAND_statement(e, lvars[1], lvars[3]))
    write_NAND_line(f, make_NAND_statement(t, lvars[2], lvars[3]))
    write_NAND_line(f, make_NAND_statement(g, t, e))
    write_NAND_line(f, make_NAND_statement(h, g, g))
    write_NAND_line(f, make_NAND_statement(lvars[0], h, d))
    return counter + 4


"""
This function should:
    TODO: keep track of counter for new vars
    TODO: write an XOR line as a series of NAND lines
    TODO: write a MAJ line as a series of NAND lines
    TODO: leave NAND lines alone
"""
def NANDify(f,prog):
    counter = 0
    for line in prog:
        if "XOR" in line:
            counter = write_XOR_as_NAND(f, line, counter)
        elif "MAJ" in line:
            counter = write_MAJ_as_NAND(f, line, counter)
        else:
            f.write(line)

"""
usage: python NANDp2NAND.py "filename.nandp"
writes "filename_converted.nand"
"""
def main():
    inname = sys.argv[1]
    name,ext = os.path.splitext(inname)
    with open(inname,'r') as infile:
        prog = infile.readlines()
    outfile = open(name+'_converted.nand','w')
    NANDify(outfile,prog)
    outfile.close()

if __name__ == "__main__":
    main()
