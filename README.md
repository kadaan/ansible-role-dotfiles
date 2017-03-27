# Ansible Role: Dotfiles

[![Build Status](https://travis-ci.org/kadaan/ansible-role-dotfiles.svg?branch=master)](https://travis-ci.org/kadaan/ansible-role-dotfiles)

Installs a set of dotfiles from a given Git repository.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    dotfiles_name: "personal"

The name of the dotfiles repository. This is used to differentiate multiple dotfiles
repositories.

    dotfiles_repo: ""

The git repository to use for retrieving dotfiles. Dotfiles should generally be laid out within the root directory of the repository.

    dotfiles_repo_accept_hostkey: true

Add the hostkey for the repo url if not already added. If ssh_opts contains "-o StrictHostKeyChecking=no", this parameter is ignored.

    dotfiles_repo_local_destination: `"{{ ansible_env.HOME }}/.dotfiles"`

The local path where the `dotfiles_repo` will be cloned.

    dotfiles_configure_osx: true

Configure OS X by running a .osx file, if it exists, in the root of the dotfiles repo.

## Dependencies


## Example Playbook

    - hosts: localhost
      roles:
        - { role: kadaan.dotfiles, dotfiles_name: personal, dotfiles_repo: "https://github.com/kadaan/dotfiles.git" }

## License

Apache 2.0
