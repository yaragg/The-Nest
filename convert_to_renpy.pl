#!/usr/bin/perl
 
#Get input
while(<>)
{
    $text = $text . $_;
}
#Removes parenthenticals
$text =~ s/\([\w+ ]+\)//g;
 
#Adds ( and ) around voice overs
$text =~ s/\(V\.O\.\) *\n*(.+)/\($1\)/g;
#If you just want the (V.O.) part removed but don't want the parentheses, comment the line above and uncomment the one below
# $text =~ s/\(V\.O\.\) *\n*(.+)/$1/g;
 
 
#Substitutes character names for aliases and quotes their dialogue.
#Simply change RILIANE to your character name and the r before "$1" to whichever alias you want
#If you need more characters, just copy and paste one of these lines and change it. Like this:
# $text =~ s/YOURCHARACTER *\n*(.+)/youralias "$1"/g;
$text =~ s/LUNA *\n*(.+)/l "$1"/g;
$text =~ s/EILHART *\n*(.+)/e "$1"/g;
$text =~ s/EMIL *\n*(.+)/em "$1"/g;
$text =~ s/NIKOLAI *\n*(.+)/n "$1"/g;
$text =~ s/ALBERT *\n*(.+)/a "$1"/g;
$text =~ s/SOLA *\n*(.+)/s "$1"/g;
$text =~ s/ALICE *\n*(.+)/a "$1"/g;
$text =~ s/SERACH *\n*(.+)/se "$1"/g;
$text =~ s/READAK *\n*(.+)/r "$1"/g;
$text =~ s/VICTORIA *\n*(.+)/v "$1"/g;
$text =~ s/VERA *\n*(.+)/ve "$1"/g;
$text =~ s/CAERS *\n*(.+)/c "$1"/g;
$text =~ s/ERIK *\n*(.+)/ek "$1"/g;

#Output result
print $text;