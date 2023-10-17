class Bitset {
    // not using std::bitset !
    vector<uint8_t> bytes;
    size_t          size;
    int             ones; // number of set bits

public:
    explicit Bitset(int size_)
    : size(size_),
      ones(0)
    {
        bytes.resize((size + 7) / 8, 0);
    }

    bool get(int idx) const
    {
        if (idx >= size)
            return false; // an exception would be the more professional approach

        size_t  pos   = idx >> 3; // div 8
        uint8_t shift = idx &  7; // mod 8
        uint8_t mask  = 1 << shift;
        return bytes[pos] & mask;
    }

    void fix(int idx)
    {
        if (idx >= size)
            return;

        size_t  pos   = idx >> 3;
        uint8_t shift = idx &  7;
        uint8_t mask  = 1 << shift;
        if (!(bytes[pos] & mask))
        {
            ones++;
            bytes[pos] |= mask;
        }
    }

    void unfix(int idx)
    {
        if (idx >= size)
            return;

        size_t  pos   = idx >> 3;
        uint8_t shift = idx &  7;
        uint8_t mask  = 1 << shift;
        if (bytes[pos] & mask)
        {
            ones--;
            bytes[pos] ^= mask;
        }
    }

    void flip()
    {
        // fast flip of whole bytes
        for (auto& i : bytes)
            i ^= 0xFF;
        // last bits beyond "size" are undefined

        ones = size - ones;
    }

    bool all() const
    {
        return ones == size;
    }

    bool one() const
    {
        return ones > 0;
    }

    int count() const
    {
        return ones;
    }

    string toString() const
    {
        string result;
        result.reserve(size);
        for (size_t i = 0; i < size; i++)
            result += get(i) ? "1" : "0";
        return result;
    }
};
