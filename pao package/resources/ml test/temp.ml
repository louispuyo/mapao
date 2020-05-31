


(* NOTE documentation cheat, how module works
////////////////////////////////////////////
Modules
module M = struct .. end module denition
module M: sig .. end= struct .. end module and signature
module M = Unix module renaming
include M include items from
module type Sg = sig .. end signature denition
module type Sg = module type of M signature of module
let module M = struct .. end in .. local module
let m = (module M : Sg) to 1
st-class module
module M = (val m : Sg) from 1
st-class module
module Make(S: Sg) = struct .. end functor
module M = Make(M') functor application
*)



(* NOTE Loops
while cond do ... done;
for var = min_value to max_value do ... done;
for var = max_value downto min_value do ... done;
*)


(* TODO *)
for var = 1 to 10 do print_newline();
print_int(var*var) done;;

(* ANCHOR *)
(*
    structure{
      <balise:name>
      <balise:arg>
      [...]
      define_op = list[]
    
      }

*)