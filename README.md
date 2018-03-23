# PyImportSortBear-With-AST

## How to use :-
```
python3 traverse.py <file_name>
```

## Example :-
```
python3 traverse.py sample.py
```

## Output :-
```
(file_input (stmt (simple_stmt (small_stmt (import_stmt (import_from from (dotted_name a) import 
(import_as_names (import_as_name b))))) NEWLINE)) (stmt (simple_stmt (small_stmt (import_stmt 
(import_from from (dotted_name c) import (import_as_names (import_as_name d))))) NEWLINE)) NEWLINE
ENDMARKER)
```
