# Meta Package
Name:           ros-jazzy-tlsf
Version:        0.9.0
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tlsf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tlsf
Requires:       ros2-jazzy-tlsf-devel

Obsoletes: ros-jazzy-tlsf < 0.9.0-1

%description
TLSF allocator version 2.4.6

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.9.0-1
- Update to latest release
