
open Str;;
let moto x = if x == 0 then print_string "x equal 0" else print_string " x equal ..";;

moto 12;;
print_newline();;
moto 0;;
print_newline();;


let tokenisation token = match token with   
">S" -> print_int(0);
| "Sf" -> print_int(3);
| _ -> print_int(1);;
(*
    => require() -> syntaxe lem
    => mactch every token -< regex
*)
tokenisation ">S" ;;
tokenisation "Sf" ;;


(*
//the tokenisation will call  python external function
:=> mustache parsing is a todo
# function

*)

let test ?(x = 0) ?(y = 0) () ?(z = 0) () = (x, y, z);;

test ~x:2 () ~z:4 ();;



(* let tmpl =
  Mustache.of_string "Hello {{name}}\n\
                      Mustache is:\n\
                      {{#qualities}}\
                      * {{name}}\n\
                      {{/qualities}}";;

let json =
  `O [ "name", `String "OCaml"
     ; "qualities", `A [ `O ["name", `String "awesome"]
                       ; `O ["name", `String "simple"]
                       ; `O ["name", `String "fun"]
                       ]
     ];;

let rendered =
  Mustache.render tmpl json;; *)


let array1 = [|1,4,2,4|];;
array1;;
(array1.(0));;

