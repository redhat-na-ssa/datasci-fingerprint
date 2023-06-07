#!/bin/bash
# set -ex

usage(){
echo "
You can run individual functions!

example:
  setup_demo
"
}

check_cd(){
  [ -d ".git" ] && return
  echo "Are you running $(basename $0) from the root path?"
  exit
}

is_sourced() {
  check_cd

  if [ -n "$ZSH_VERSION" ]; then 
      case $ZSH_EVAL_CONTEXT in *:file:*) return 0;; esac
  else  # Add additional POSIX-compatible shell names here, if needed.
      case ${0##*/} in dash|-dash|bash|-bash|ksh|-ksh|sh|-sh) return 0;; esac
  fi
  return 1  # NOT sourced.
}

setup_venv(){
  python3 -m venv venv
  source venv/bin/activate
  pip install -q -U pip

  check_venv || usage
}

check_venv(){
  # activate python venv
  [ -d venv ] && . venv/bin/activate || setup_venv
}


setup_dataset(){
  SCRATCH=scratch
  DATA_SRC=https://github.com/redhat-na-ssa/datasci-fingerprint-data.git
  CLONE_PATH="${SCRATCH}/_raw"
  
  echo "Pulling dataset from ${DATA_SRC}..."

  git clone "${DATA_SRC}" "${CLONE_PATH}" >/dev/null 2>&1 || echo "exists"

  mkdir -p "${SCRATCH}"/{train,models}

  tar -Jxf "${CLONE_PATH}"/left.tar.xz -C "${SCRATCH}"/train/ && \
  tar -Jxf "${CLONE_PATH}"/right.tar.xz -C "${SCRATCH}"/train/ && \
  tar -Jxf "${CLONE_PATH}"/real.tar.xz -C "${SCRATCH}" && \
  tar -Jxf "${CLONE_PATH}"/model-v1-full.tar.xz -C "${SCRATCH}"/models

}

install_requirements(){
  pip install -qr requirements.txt
}

print_info(){
  echo "
  Run the following:

  # activate python virtual env (bash)
  source venv/bin/activate

  # blastoff w/ jupyter
  jupyter-lab
  "
}

setup_demo(){
  check_cd
  check_venv
  setup_dataset  
  install_requirements
  print_info
}

is_sourced && usage || setup_demo
