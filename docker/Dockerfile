# Dockerfile to create image of the local computational environment
# for pre- and post-processing steps and to submit jobs to Azure Batch.

FROM barbagroup/petibm:0.5.1-GPU-OpenMPI-xenial
MAINTAINER Olivier Mesnard <mesnardo@gwu.edu>

# Install base system.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        build-essential \
        autotools-dev \
        gfortran \
        vim \
        git \
        wget \
        curl \
        pkg-config

# Set name of the conda environment to create.
ENV CONDA_ENV=py37-snakelips

# Install Miniconda3 (4.8.2).
ENV MINICONDA_DIR=/opt/miniconda3
RUN VERSION=4.8.2 && \
    FILENAME=Miniconda3-py37_${VERSION}-Linux-x86_64.sh && \
    URL=https://repo.anaconda.com/miniconda/${FILENAME} && \
    wget ${URL} -P /tmp && \
    bash /tmp/${FILENAME} -b -p ${MINICONDA_DIR} && \
    echo "source ${MINICONDA_DIR}/etc/profile.d/conda.sh" >> /root/.bashrc && \
    echo "conda activate ${CONDA_ENV}" >> /root/.bashrc && \
    rm -f /tmp/${FILENAME}

# Create conda environment.
RUN . ${MINICONDA_DIR}/bin/activate && \
    conda create --name=${CONDA_ENV} \
        python=3.7 \
        h5py=2.10.0 \
        lxml=4.5.0 \
        matplotlib=3.1.3 \
        numpy=1.18.1 \
        pyyaml=5.3.1 \
        scipy=1.4.1

# Install Azure-CLI (2.3.1).
RUN . ${MINICONDA_DIR}/bin/activate && \
    conda activate ${CONDA_ENV} && \
    pip install azure-cli==2.3.1 && \
    conda deactivate

# Install Batch-Shipyard (3.9.1).
ADD shipyard-install.sh /tmp
RUN VERSION=3.9.1 && \
    TARBALL=${VERSION}.tar.gz && \
    URL=https://github.com/Azure/batch-shipyard/archive/${TARBALL} && \
    wget ${URL} -P /tmp && \
    SRCDIR=/opt/batch-shipyard/${VERSION} && \
    mkdir -p ${SRCDIR} && \
    tar -xzf /tmp/${TARBALL} -C ${SRCDIR} --strip-components=1 && \
    /bin/bash /tmp/shipyard-install.sh -d ${SRCDIR} -c ${MINICONDA_DIR} -e ${CONDA_ENV} && \
    rm -f /tmp/shipyard-install.sh /tmp/${TARBALL}

ENV PATH=/root/.local/bin:${PATH}

# Install PetibmPy (0.2).
RUN VERSION=0.2 && \
    TARBALL=v${VERSION}.tar.gz && \
    URL=https://github.com/mesnardo/petibmpy/archive/${TARBALL} && \
    wget ${URL} -P /tmp && \
    SRCDIR=/opt/petibmpy/${VERSION} && \
    mkdir -p ${SRCDIR} && \
    tar -xzf /tmp/${TARBALL} -C ${SRCDIR} --strip-components=1 && \
    cd ${SRCDIR} && \
    . ${MINICONDA_DIR}/bin/activate && \
    conda activate ${CONDA_ENV} && \
    python setup.py install && \
    conda deactivate && \
    rm -f /tmp/${TARBALL}

# Add helper script to delete directory recursively on Azure Storage.
ADD az-storage-directory-delete /root/.local/bin
