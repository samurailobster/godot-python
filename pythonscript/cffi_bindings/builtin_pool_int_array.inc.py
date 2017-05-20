
class PoolIntArray(BaseBuiltin):
    GD_TYPE = lib.GODOT_VARIANT_TYPE_POOL_INT_ARRAY

    def __init__(self):
        self._gd_ptr = ffi.new('godot_pool_int_array*')
        lib.godot_pool_int_array_new(self._gd_ptr)


    def __repr__(self):
        return "<%s()>" % (type(self).__name__)

    def __eq__(self, other):
        return isinstance(other, PoolIntArray) and lib.godot_pool_int_array_operator_equal(self._gd_ptr, other._gd_ptr)

    # Properties

    # Methods
