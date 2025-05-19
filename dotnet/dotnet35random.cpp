#include <cstdint>

extern "C" {

__declspec(dllexport) struct DotNet35Random {
    static const int MBIG = 2147483647; // int.MaxValue
    static const int MSEED = 161803398;

    int SeedArray[56];
    int inext;
    int inextp;

    // Initialize with seed
    void init(int seed) {
        int num = MSEED - (seed < 0 ? -seed : seed);
        SeedArray[55] = num;
        int num2 = 1;
        for (int i = 1; i < 55; i++) {
            int num3 = (21 * i) % 55;
            SeedArray[num3] = num2;
            num2 = num - num2;
            if (num2 < 0)
                num2 += MBIG;
            num = SeedArray[num3];
        }
        for (int j = 0; j < 4; j++) {
            for (int k = 1; k < 56; k++) {
                SeedArray[k] -= SeedArray[1 + (k + 30) % 55];
                if (SeedArray[k] < 0)
                    SeedArray[k] += MBIG;
            }
        }
        inext = 0;
        inextp = 31;
    }

    // Sample function, returns double in [0,1)
    double Sample() {
        if (++inext >= 56) inext = 1;
        if (++inextp >= 56) inextp = 1;

        int num = SeedArray[inext] - SeedArray[inextp];
        if (num < 0) num += MBIG;

        SeedArray[inext] = num;

        return (double)num * 4.656612875245797E-10; // 1/(MBIG+1)
    }

    // Equivalent to Next()
    int Next() {
        return (int)(Sample() * MBIG);
    }

    // Next with maxValue
    int NextMax(int maxValue) {
        if (maxValue < 0) return 0; // or error
        return (int)(Sample() * maxValue);
    }

    // Next with min and max
    int NextMinMax(int minValue, int maxValue) {
        if (minValue > maxValue) return minValue; // or error
        unsigned int num = (unsigned int)(maxValue - minValue);
        if (num <= 1) return minValue;
        return (int)((unsigned int)(Sample() * num) + minValue);
    }
};

// Functions to create and free RNG objects
__declspec(dllexport) DotNet35Random* rng_create(int seed) {
    DotNet35Random* rng = new DotNet35Random();
    rng->init(seed);
    return rng;
}

__declspec(dllexport) void rng_free(DotNet35Random* rng) {
    delete rng;
}

__declspec(dllexport) double rng_sample(DotNet35Random* rng) {
    return rng->Sample();
}

__declspec(dllexport) int rng_next(DotNet35Random* rng) {
    return rng->Next();
}

__declspec(dllexport) int rng_next_max(DotNet35Random* rng, int maxValue) {
    return rng->NextMax(maxValue);
}

__declspec(dllexport) int rng_next_minmax(DotNet35Random* rng, int minValue, int maxValue) {
    return rng->NextMinMax(minValue, maxValue);
}
}
