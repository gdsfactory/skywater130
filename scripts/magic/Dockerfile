FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PDK_ROOT=/opt/pdk

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3 \
    tcl-dev \
    tk-dev \
    libcairo2-dev \
    libx11-dev \
    libxpm-dev \
    libglu1-mesa-dev \
    m4 \
    csh \
    && rm -rf /var/lib/apt/lists/*

# Build Magic
RUN git clone --depth 1 https://github.com/RTimothyEdwards/magic.git /tmp/magic && \
    cd /tmp/magic && \
    ./configure && \
    make -j$(nproc) && \
    make install && \
    rm -rf /tmp/magic

# Build open_pdks (sky130A only — takes a while)
RUN git clone --depth 1 https://github.com/RTimothyEdwards/open_pdks.git /tmp/open_pdks && \
    cd /tmp/open_pdks && \
    ./configure --enable-sky130-pdk --with-sky130-variants=A && \
    make -j$(nproc) && \
    make install && \
    rm -rf /tmp/open_pdks

# Verify Magic works
RUN echo 'puts "Magic OK: [info patchlevel]"; quit -noprompt' | magic -dnull -noconsole

WORKDIR /work
COPY sweep_params.json /work/sweep_params.json
COPY generate_references.sh /work/generate_references.sh
RUN chmod +x /work/generate_references.sh

# Output goes to /output (mount as volume)
ENV REF_DIR=/output

ENTRYPOINT ["/work/generate_references.sh"]
