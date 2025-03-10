# MTUOC-utils

A set of programs intended for users with no knowledge of Unix/Linux terminal. Each program performs some useful Unix commands or combination of programs for corpus processing. All the programs have a simple GUI interface and binaries for Windows and Mac are distributed in the latests releases.

## MTUOC-word-count

It counts lines, words and characters in text files. It can handle very large files. It performs the same process than Unix's

`wc file.txt`

although results may be slightly different.

The GUI interface asks for the file to process with the button **Select File**, and after selecting the file it shows the Lines, Words and Characters.

## MTUOC-file-viewer

It shows the content of text file and it can manage files of any size with no memory issues. It performs the same process thant the Unix's commands: `cat`, `more` and `tail`.

To use the program the file to be viewed should be selected with the button **Select file**. To see the content in a continuous manner use the button **Cat** and stop the view with the button **Stop**. You can see the file from the beginning with the button **More** and each time you click on this button the program will show the next lines. Reversely, to see the file from the end you can use the button **Tail**, and each time you click on this button the program will show the preceding lines.

## MTUOC-Moses2tabtxt-GUI

It converts two Moses files (one for the source and another for the target language) into a tabbed text file. It performs the same process than the `paste` Unix command. To use the program, select the source file with the **Browse** button of the Input File 1, the target file with the **Browse** button of the Input File 2 and the output file with the **Browse** button of the Output file. Then click the **Process** button and the tabbed text file will be created.

## MTUOC-cat-GUI

This program allows to concatenate two or more files into a single output file. You can add the files to be concatenated with the **Add File** button, or remove all the files of the list with the button **Clear Files**. Use the **Browse** button to select the output file and the button **Concatenate files** to concatenate the files. The output file will contain the concatenation of the files.

## MTUOC-sort-uniq-shuf

This program can perform the following Unix commands or combination of commands over a file: `sort`, `sort | uniq` and `sort | uniq | shuf`. That is, the program is able to sort, to remove duplicate lines, and to randomize the order of the lines of a file.

Select the input file with the **Open** button and the output file with the **Save** button. If you want to sort the file click on the **Go!** button; if you want to remove repetitions, mark the **unic** option and to randomize the lines select the **shuf** option before clicking on **Go!**.






