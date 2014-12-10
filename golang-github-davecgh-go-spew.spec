%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         davecgh
%global repo            go-spew
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          83f84dc933714d51504ceed59f43ead21d096fe7
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging
License:        ISC
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/spew) = %{version}-%{release}
Provides:       golang(%{import_path}/spew/testdata) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav spew %{buildroot}/%{gopath}/src/%{import_path}/

%check
# NOTE in spew/testdata/dumpcgo.go
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/spew

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git83f84dc
- First package for Fedora
  resolves: #1172198
