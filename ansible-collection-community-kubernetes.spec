Name:           ansible-collection-community-kubernetes
Version:        1.1.1
Release:        1
Summary:        Kubernetes Collection for Ansible.
License:        UNKNOWN
URL:            https://galaxy.ansible.com/community/kubernetes
Source0:        https://galaxy.ansible.com/download/ansible-collection-community-kubernetes-%{version}.tar.gz
BuildArch:      noarch

Requires:       ansible


%description
Kubernetes Collection for Ansible.

%prep
%autosetup -c ansible-collection-community-kubernetes-%{version}-%{release}

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/community/kubernetes/
cp -rp * %{buildroot}/%{_datadir}/ansible/collections/ansible_collections/community/kubernetes/

%files
%license LICENSE
%doc README.md
%{_datadir}/ansible/collections/ansible_collections/community/kubernetes/


%changelog
