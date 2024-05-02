# Meta Package
Name:           ros-jazzy-test-interface-files
Version:        0.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-test_interface_files and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-test_interface_files
Requires:       ros2-jazzy-test_interface_files-devel

Obsoletes: ros-jazzy-test-interface-files < 0.11.0-1

%description
A package containing message definitions and fixtures used exclusively
for testing purposes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.11.0-1
- Update to latest release
