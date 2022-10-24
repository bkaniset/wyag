import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib


argparser = argparse.ArgumentParser(description="Content Parser")

argsubparsers = argparser.add_subparsers(title="commands",dest="command")
argsubparsers.required  = True

def main(argv=sys.argv[1:]):
     args = argparser.parse_args(argv)
     
     if     args.comand    ==   "add"                 : comd_add(args)
     elif  args.command  ==   "cat-file"            : cmd_cat_file(args) 
     elif  args.command  ==   "commit"           : cmd_checkout(args)
     elif  args.command  ==   "hash-object"     : cmd_hash_object(args)
     elif  args.command  ==   "init"                  : cmd_init(args)
     elif  args.command  ==   "log"                  : cmd_log(args)
     elif  args.command  ==   "ls-tree"              : cmd_ls_tree(args)
     elif  args.command  ==   "merge"              : cmd_merge(args)
     elif  args.command  ==   "rebase"             : cmd_rebase(args)
     elif  args.command  ==   "rev-parse"         : cmd_rev_parse(args)
     elif  args.command  ==   "rm"                   : cmd_rm(args)
     elif  args.command  ==   "show-ref"           : cmd_show_ref(args)
     elif  args.command  ==   "tag"                   :  cmd_tag(args)
     
     
     
     
     
     
     
     
     
     
     
