# ComputerDesign

There some things that maybe wont work on another machine so let me know if something doesn't work.

INSTALLING THE VSCODE EXTENSION:
    open ComputerDesign in vscode, right-click 'extensionOVT-0.0.1.vsix' in the explorer and choose the option at the bottom 'install extension VSIX' and after that add SOMEPATH\ComputerDesign\python\regi to PATH. from now on the shortcut 'ctrl+f7' or 'cmd+f7' will compile a .high file and assemble a .rasm file as long as youre cursor is inside the file while doing so (because the texteditor must be active). 

SIMULATING PROGRAMS:
logisim:
    pretty slow but both OVERTURE and Regi are originally made in logisim.
    you should be able to simulate both. OVERTURE is called OVERTURE.circ and an old version of Regi is called 'Logisim/V232bitfloatstack - Copy - Copy.circ' because why would I use good names, I wasn't planning on sharing this.
    To load a program click on the ROM and use the 'machinecode.ovt' file as data file. (assembling will automatically wrtite to here)
Digital:
    Only Regi is available in Digital. The reason I ported to digital is that digital is conservitavely 1000 times faster in simuating.
    To simulate open any .dig file in the digital/computer folder starting with 'computer' using digital. (assembling will automatically wrtite to here)

 ---------------------------------
ADVANCED:
COMPILING AND ASSEMBLING:
overture:
    in the python folder is a folder named OVERTURE. You can use both assembly.ovt and editor.py to write code. There is example code in the 'programmas' folder
    To assemble you run assembler+interpreter.py, it should automatically write the machinecode both to machinecode.out in the same folder and to machinecode.ovt in the logisim folder.
regi:
    There is a lot going on in the regi python folder 'higher_programs' and 'programma's' have example programs, in high and assembly respectively. (high is a language that gets compiled to assembly, it's based on python).
    some programs may not work because they were made for older versions of RASM.
    hcompiler.py will compile high.ovt to assembly and write it to assembly.ovt.
    assemblerimport.py will assemble assembly.ovt together with any code you 'import' and it finds in the programs folder.
    It assembles it and should write it to machinecode.out, \Logisim\MachineCode.ovt and \Digital\computer\RomData.hex at the same times.
    I doubt it works but high2py.py should eventually compile high.ovt to python code in py.py

