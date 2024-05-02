# Meta Package
Name:           ros-humble-libyaml-vendor
Version:        1.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/yaml/libyaml
Summary:        Meta package for ros2-humble-libyaml_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-libyaml_vendor
Requires:       ros2-humble-libyaml_vendor-devel

Obsoletes: ros-humble-libyaml-vendor < 1.2.2-1

%description
Vendored version of libyaml.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.2-1
- Initial humble build
