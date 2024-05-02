# Meta Package
Name:           ros-iron-test-interface-files
Version:        0.10.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-test_interface_files and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-test_interface_files
Requires:       ros2-iron-test_interface_files-devel

Obsoletes: ros-iron-test-interface-files < 0.10.2-1

%description
A package containing message definitions and fixtures used exclusively
for testing purposes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.10.2-1
- Update to latest release
