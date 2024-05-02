# Meta Package
Name:           ros-humble-yaml-cpp-vendor
Version:        8.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/jbeder/yaml-cpp
Summary:        Meta package for ros2-humble-yaml_cpp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-yaml_cpp_vendor
Requires:       ros2-humble-yaml_cpp_vendor-devel

Obsoletes: ros-humble-yaml-cpp-vendor < 8.0.2-1

%description
Wrapper around yaml-cpp, it provides a fixed CMake module and an
ExternalProject build of it.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.8.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.8.0.2-1
- update to latest upstream release
* Fri Jun 30 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.8.0.2-1
- update to latest upstream release
