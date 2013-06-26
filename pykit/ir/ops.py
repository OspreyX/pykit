#===------------------------------------------------------------------===
# Typed IR (initial input)
#===------------------------------------------------------------------===

# IR Constants. Constants start with an uppercase letter

# math
Sin                = 'Sin'
Asin               = 'Asin'
Sinh               = 'Sinh'
Asinh              = 'Asinh'
Cos                = 'Cos'
Acos               = 'Acos'
Cosh               = 'Cosh'
Acosh              = 'Acosh'
Tan                = 'Tan'
Atan               = 'Atan'
Atan2              = 'Atan2'
Tanh               = 'Tanh'
Atanh              = 'Atanh'
Log                = 'Log'
Log2               = 'Log2'
Log10              = 'Log10'
Log1p              = 'Log1p'
Exp                = 'Exp'
Exp2               = 'Exp2'
Expm1              = 'Expm1'
Floor              = 'Floor'
Ceil               = 'Ceil'
Abs                = 'Abs'
Erfc               = 'Erfc'
Rint               = 'Rint'
Pow                = 'Pow'
Round              = 'Round'

# ______________________________________________________________________
# Constants

constant           = 'constant'         # (object pyval)

# ______________________________________________________________________
# Variables

alloca             = 'alloca'           # (expr n)
load               = 'load'             # (alloc var)
store              = 'store'            # (alloc var, expr value)
# phi is below

# ______________________________________________________________________
# Primitives

# Arrays/lists
map                = 'map'              # (fn func, expr arrays, const axes)
reduce             = 'reduce'           # (fn func, expr array, const axes)
scan               = 'scan'             # (fn func, expr array, const axes)
allpairs           = 'allpairs'         # (fn func, expr array, const axes)

# Scalars
min                = 'min'              # expr *args
max                = 'max'              # expr *args

print_             = 'print_'           # expr *values

# ______________________________________________________________________
# Containers

### TODO: This should be library code instead ?
# No matter how we do this, we'll end up reinventing pypy.

# ______________________________________________________________________
# Boxing and coercion

box                = 'box'              # (expr arg)
unbox              = 'unbox'            # (expr arg)
convert            = 'convert'          # (expr arg)

# ______________________________________________________________________
# Constructors

new_list           = 'new_list'         # (expr elems)
new_tuple          = 'new_tuple'        # (expr elems)
new_dict           = 'new_dict'         # (expr keys, expr values)
new_set            = 'new_set'          # (expr elems)

new_string         = 'new_string'       # (expr string)
new_unicode        = 'new_unicode'      # (expr string)

new_object         = 'new_object'       # (expr args)
new_struct         = 'new_struct'       # (expr *initializers)
new_complex        = 'new_complex'      # (expr real, expr imag)
new_data           = 'new_data'         # (expr size)

# ______________________________________________________________________
# Control flow

# Basic block leaders
phi                = 'phi'              # (expr blocks, expr values)
exc_setup          = 'exc_setup'        # (block *handlers)
exc_catch          = 'exc_catch'        # (expr *types)

# Basic block terminators
jump               = 'jump'             # (str target)
cbranch            = 'cbranch'          # (expr test, str true_target,
                                        #  str false_target)
exc_throw          = 'exc_throw'        # (expr exc, expr *args)
ret                = 'ret'              # (expr result)

# ______________________________________________________________________
# Functions

function           = 'function'         # (str funcname)
partial            = 'partial'          # (fn function, expr *vals)
# virtual_method     = 'virtual_method'   # (expr extobj, string methname)
func_from_addr     = 'func_from_addr'   # (expr pointer)

call               = 'call'             # (expr obj, expr *args)
call_obj           = 'call_obj'         # (expr obj, expr args, expr kwds)
call_virtual       = 'call_virtual'     # (fn method, expr args, expr kwds)
call_external      = 'call_external'    # (str name, expr *args)
call_math          = 'call_math'        # (str func, expr *args)

# ______________________________________________________________________
# Pointers

ptradd             = 'ptradd'           # (expr pointer, expr addition)
ptrload            = 'ptrload'          # (expr pointer)
ptrstore           = 'ptrstore'         # (expr pointer, expr value)
ptrcast            = 'ptrcast'          # (expr pointer)
ptr_isnull         = 'ptr_isnull'       # (expr' pointer)

# ______________________________________________________________________
# Iterators

getiter            = 'getiter'          # (expr obj)
next               = 'next'             # (iter it)

# ______________________________________________________________________
# Generators

yieldval           = 'yieldval'         # (expr value)
yieldfrom          = 'yieldfrom'        # (expr value)

# ______________________________________________________________________
# Attributes

getfield           = 'getfield'         # (expr value, str attr)
setfield           = 'setfield'         # (expr value, str attr, expr value)

# ______________________________________________________________________
# Indexing

getindex           = 'getindex'         # (expr value, expr indices)
setindex           = 'setindex'         # (expr value, expr indices, expr value)
getslice           = 'getslice'         # (expr value, expr indices)
setslice           = 'setslice'         # (expr value, expr indices, expr value)

slice              = 'slice'            # (expr lower, expr upper, expr step)
# newaxis            = 'newaxis'        # => const(None)

# ______________________________________________________________________
# Basic operators

# Use prefix to avoid clashes with builtins...

# Binary
add                = 'add'
sub                = 'sub'
mul                = 'mul'
div                = 'div'
floordiv           = 'floordiv'
mod                = 'mod'
lshift             = 'lshift'
rshift             = 'rshift'
bitand             = 'bitand'
bitor              = 'bitor'
bitxor             = 'bitxor'
and_               = 'and_'

# Unary
invert             = 'invert'
not_               = 'not_'
uadd               = 'uadd'
usub               = 'usub'

# Compare
eq                 = 'eq'
noteq              = 'noteq'
lt                 = 'lt'
lte                = 'lte'
gt                 = 'gt'
gte                = 'gte'
is_                = 'is_'
isnot              = 'isnot'
in_                = 'in_'
notin              = 'notin'

# ______________________________________________________________________
# Closures

# Activation frame, manipulate using getfield/setfield
make_frame         = 'make_frame'       # (frame parent, string names)
make_cell          = 'make_cell'        # ()
load_cell          = 'load_cell'        # (expr cell)
store_cell         = 'store_cell'       # (expr cell, expr value)

# ______________________________________________________________________
# Threads

threadpool_start   = 'threadpool_start' # (expr nthreads)
threadpool_submit  = 'threadpool_submit' # (expr threadpool, fn function)
threadpool_join    = 'threadpool_join'  # (expr threadpool)
threadpool_close   = 'threadpool_close' # (expr threadpool)
thread_start       = 'thread_start'     # (fn function)
thread_join        = 'thread_join'      # (expr thread)

#===------------------------------------------------------------------===
# Low-level IR
#===------------------------------------------------------------------===

# Low-level result:
#   - no objects, arrays, complex numbers
#   - no builtins
#   - no frames
#   - no map, reduce, scan, or yield

check_overflow     = 'check_overflow'   # (expr arg)

load_vtable        = 'load_vtable'      # (expr obj)
vtable_lookup      = 'vtable_lookup'    # (expr vtable, str method)

# ______________________________________________________________________
# Garbage collection

# Refcounting
gc_gotref          = 'gc_gotref'        # (expr arg)
gc_giveref         = 'gc_giveref'       # (expr arg)
gc_incref          = 'gc_incref'        # (expr obj)
gc_decref          = 'gc_decref'        # (expr obj)

# GC
gc_alloc           = 'gc_alloc'         # (expr n)
gc_dealloc         = 'gc_dealloc'       # (expr value)
gc_collect         = 'gc_collect'
gc_write_barrier   = 'gc_write_barrier'
gc_read_barrier    = 'gc_read_barrier'
gc_traverse        = 'gc_traverse'

# ______________________________________________________________________
# Opcode utils

is_leader     = lambda x: x in (phi, exc_setup, exc_catch)
is_terminator = lambda x: x in (jump, cbranch, exc_throw, ret)
is_void       = lambda x: is_terminator(x) or x in (print_, store)