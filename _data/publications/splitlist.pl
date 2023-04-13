#!/usr/bin/perl -w

open(IN, "../list_long.yml") or die;
while(<IN>) {
  
  if (/- id/) {
    close(OUT);
    @parts = split(/:/,$_);
    $id = $parts[1];
    chomp($id);
    $idfile = $id.".yml";
    print("$idfile\n");
    open(OUT,">$idfile") or die;
    print OUT $_;
  } else {
    print OUT $_;
  }
  
}
