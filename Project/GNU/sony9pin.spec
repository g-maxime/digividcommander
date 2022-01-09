# Copyright (c) 2022 info@mediaarea.net
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# norootforbuild

%global sony9pin_version 1.0

Name:          sony9pin
Version:       %sony9pin_version
Release:       1
Summary:       Control Sony capture deck over serial interface
Group:         Productivity/Multimedia/Other
License:       MIT
URL:           https://mipops.github.io/digividcommander
Packager:      Jerome Martinez <info@mediaarea.net>
Source0:       sony9pin_%{version}-1.tar.gz
Prefix:        %{_prefix}
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5SerialPort)

%description
sony9pin control sony capture deck over serial interface

%prep
%setup -q -n sony9pin
%build

# build CLI
mkdir -p tools/sony9pin/build
pushd tools/sony9pin/build
    qmake-qt5  QMAKE_CXXFLAGS+="-g $RPM_OPT_FLAGS" ..
    %__make %{?jobs:-j%{jobs}} 
popd

%install
%__install -D -m 755 tools/sony9pin/build/sony9pin %{buildroot}%{_bindir}/sony9pin

%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%files
%defattr(-,root,root,-)
%{_bindir}/sony9pin

%changelog
* Sat Jan 01 2022 Jerome Martinez <info@mediaarea.net> - 1.0-1
- Initial release
