# Meta Package
Name:           ros-iron-yaml-cpp-vendor
Version:        8.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/jbeder/yaml-cpp
Summary:        Meta package for ros2-iron-yaml_cpp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-yaml_cpp_vendor
Requires:       ros2-iron-yaml_cpp_vendor-devel

Obsoletes: ros-iron-yaml-cpp-vendor < 8.1.2-1

%description
Wrapper around yaml-cpp, it provides a fixed CMake module and an
ExternalProject build of it.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.8.1.2-1
- Update to latest release
