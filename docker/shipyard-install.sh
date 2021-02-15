#!/usr/bin/env bash
# Install Batch Shipyard within conda environment.
# Creates a symbolink link in $HOME/.local/bin.

print_usage() {
    printf "Usage: [-d] Batch Shipyard directory [-c] Conda directory [-e] Conda environment name\n"
}

pkgdir=""
condadir=""
envname=""

while getopts 'd:c:e:h' flag; do
    case "${flag}" in
        d) pkgdir=`realpath "${OPTARG}"` ;;
        c) condadir=`realpath "${OPTARG}"` ;;
        e) envname=${OPTARG} ;;
        h) print_usage
           exit 0 ;;
        *) print_usage
           exit 1 ;;
    esac
done

printf "*** Batch Shipyard installation ***\n"
printf "Batch Sipyard directory: ${pkgdir}\n"
printf "Conda directory: ${condadir}\n"
printf "Name of Conda environment: ${envname}\n\n"

source $condadir/bin/activate base

cd $pkgdir

cat > get_shipyard_version.py <<- EOM
from convoy import version

if __name__ == "__main__":
    print(version.__version__)
EOM

version=$((python get_shipyard_version.py) 2>&1)
rm -f get_shipyard_version.py

bindir="$HOME/.local/bin"
mkdir -p $bindir
execname="shipyard${version//./}"


conda activate $envname
pip install --upgrade setuptools
pip install --upgrade -r requirements.txt
pip install --upgrade --no-deps -r req_nodeps.txt
conda deactivate

cat > $bindir/$execname <<- EOM
#!/usr/bin/env bash

source $condadir/bin/activate base

set -e
set -f

BATCH_SHIPYARD_ROOT_DIR=$pkgdir

if [ -z \$BATCH_SHIPYARD_ROOT_DIR ]; then
    echo Batch Shipyard root directory not set.
    echo Please rerun the install.sh script.
    exit 1
fi

conda activate $envname
python3 \$BATCH_SHIPYARD_ROOT_DIR/shipyard.py \$*
conda deactivate
EOM

chmod +x $bindir/$execname
rm -f $bindir/shipyard
ln -s $bindir/$execname $bindir/shipyard

exit 0
