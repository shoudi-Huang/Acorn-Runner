#! /usr/bin/env sh
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################"
echo ""
count=0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `tests_e2e` directory

for test in tests_e2e/*.in; do
    name=$(basename $test .in)
    config=tests_e2e/$name.config
    expected=tests_e2e/$name.out

    python3 run.py $config < $test | diff - $expected || echo "Test $name: failed!\n" 

    count=$((count+1))
done

echo "Finished running $count tests!"
