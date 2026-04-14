# Reference GDS generation for XOR validation.
#
# Builds Magic VLSI + open_pdks at PINNED commits to produce deterministic
# device geometry. The committed ref_gds/ files were generated from exactly
# these versions. Updating either commit WILL change geometry and require
# regenerating all reference GDS + fixing any XOR deltas.
#
# Usage:
#   docker build -t sky130-magic-ref scripts/magic/
#   docker run --rm -e PDK_ROOT=/usr/local/share/pdk \
#     -v $(pwd)/tests/ref_gds:/output sky130-magic-ref

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# ── Pinned upstream commits ──────────────────────────────────────────────
# CHANGING THESE WILL INVALIDATE ALL REFERENCE GDS.
# If you bump these, you must regenerate refs and fix any XOR failures.
ARG MAGIC_COMMIT=67c6ed939514e537773f9f01cc2ecca5c3400c44
ARG OPEN_PDKS_COMMIT=fc20c144baf309002e0b335585a3aaef06b56f00
# ─────────────────────────────────────────────────────────────────────────

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

# Build Magic at pinned commit
RUN git clone https://github.com/RTimothyEdwards/magic.git /tmp/magic && \
    cd /tmp/magic && \
    git checkout ${MAGIC_COMMIT} && \
    ./configure && \
    make -j$(nproc) && \
    make install && \
    rm -rf /tmp/magic

# Build open_pdks at pinned commit (sky130A only)
RUN git clone https://github.com/RTimothyEdwards/open_pdks.git /tmp/open_pdks && \
    cd /tmp/open_pdks && \
    git checkout ${OPEN_PDKS_COMMIT} && \
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
