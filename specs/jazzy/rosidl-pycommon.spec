# Meta Package
Name:           ros-jazzy-rosidl-pycommon
Version:        4.6.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_pycommon and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_pycommon
Requires:       ros2-jazzy-rosidl_pycommon-devel

Obsoletes: ros-jazzy-rosidl-pycommon < 4.6.1-1

%description
Common Python functions used by rosidl packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
