(* pao interpreter v1.0 *)

val section:  

module Astack :
    sig
      type 'a t
      val create : unit -> 'a t
      val push : 'a -> 'a t -> unit
      val pop : 'a t -> 'a
    end = Stack;;

  
  let i = 0;;
  let parser str = 
  let str2 = str.[i] in function 
  "<$" -> print_string("start");
| "/>" -> print_string("end");
| _ -> print_char(str2);;

let parserex = parser "<$ some action />";;
(parserex);;

let formater arg = match arg with
"<$" -> arg;
| _ -> "";;

let c = formater "<$";;
print_string(c);;


module type CLIENT =            (* client's view *)
  sig
    type t
    type currency
    val deposit : t -> currency -> currency
    val retrieve : t -> currency -> currency
  end;;

module type BANK =            (* banker's view *)
  sig
    include CLIENT
    val create : unit -> t
  end;;

module Veta =
struct
  (*here we have the structure*)
end


module type V_Veta =
sig
  type priot

end;;


class point x_init = 
object
val mutable x = x_init
method get_x = x
method get_offset = x - x_init
method move d = x <- x+d
end;;

module StringMap = Map.Make(String)
module Graphql = struct

