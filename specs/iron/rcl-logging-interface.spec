# Meta Package
Name:           ros-iron-rcl-logging-interface
Version:        2.5.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl_logging_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl_logging_interface
Requires:       ros2-iron-rcl_logging_interface-devel

Obsoletes: ros-iron-rcl-logging-interface < 2.5.1-1

%description
Interface that rcl_logging backends needs to implement.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.1-1
- Update to latest release
