# Meta Package
Name:           ros-iron-pybind11-vendor
Version:        3.0.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/pybind/pybind11
Summary:        Meta package for ros2-iron-pybind11_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pybind11_vendor
Requires:       ros2-iron-pybind11_vendor-devel

Obsoletes: ros-iron-pybind11-vendor < 3.0.3-1

%description
Wrapper around pybind11.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.0.3-1
- Update to latest release
