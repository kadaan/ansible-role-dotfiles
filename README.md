# Ansible Role: Dotfiles

[![CI][badge-gh-actions]][link-gh-actions]

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
        - { role: kadaan.dotfiles, dotfiles_execute: true }

## License

Apache 2.0

[badge-gh-actions]: https://github.com/kadaan/ansible-role-dotfiles/workflows/CI/badge.svg?event=push
[link-gh-actions]: https://github.com/kadaan/ansible-role-dotfiles/actions?query=workflow%3ACI