# Meta Package
Name:           ros-jazzy-zenoh-cpp-vendor
Version:        0.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-zenoh_cpp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-zenoh_cpp_vendor
Requires:       ros2-jazzy-zenoh_cpp_vendor-devel

Obsoletes: ros-jazzy-zenoh-cpp-vendor < 0.2.3-1

%description
Vendor pkg to install zenoh-cpp

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.2.3-1
- Update to latest release
* Sun Mar 02 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.2.2-1
- Update to latest release
